import json_manager
import click
import os
import click
@click.group()
def main():
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar la consola
    click.echo("=================================")
    click.echo("      ¡Bienvenido a la App!      ")
    click.echo("=================================")
    click.echo("Aquí puedes gestionar tus usuarios.")
    click.echo("=================================")

@main.command()
def users():
    data = json_manager.read_json('data.json')
    for user in data:
        print(f'{user["id"]} - {user["name"]} - {user["lastname"]}')

@main.command()
@click.option('--name', required=True, help=' Nombre del usuario')
@click.option('--lastname', required=True, help=' Apellido del usuario')
@click.pass_context
def new_user(ctx, name, lastname):
    if not name or not lastname:
        ctx.fail('El nombre y el apellido son obligatorios')
    else:
        data = json_manager.read_json('data.json')
        id = len(data) + 1
        new_user = {
            'id': id,
            'name': name,
            'lastname': lastname
        }

        data.append(new_user)
        json_manager.write_json('data.json', data)
        click.echo(f'Usuario {name} {lastname} creado exitosamente con id {id}')

@main.command()
@click.argument('id', type=int)
def get_user(id):
    data = json_manager.read_json('data.json')
    user = next((user for user in data if user['id'] == id), None)
    if user is None:
        click.echo(f'El usuario con id {id} no existe')
    else:
        print(f'{user["id"]} - {user["name"]} - {user["lastname"]}')

@main.command()
@click.argument('id', type=int)
def delete_user(id):
    data = json_manager.read_json('data.json')
    user = next((user for user in data if user['id'] == id), None)
    if user is None:
        click.echo(f'El usuario con id {id} no existe')
    else:
        data.remove(user)
        json_manager.write_json('data.json', data)
        click.echo('--------------------------------')
        click.echo('Usuarios actuales:')
        click.echo('--------------------------------')
        for user in data:
            print(f'* {user["id"]} - {user["name"]} - {user["lastname"]}')
        click.echo(f'El usuario con id {id} ha sido eliminado')
        
@main.command()
@click.argument('id', type=int)
@click.option('--name', required=False, help='Nombre del usuario')
@click.option('--lastname', required=False, help='Apellido del usuario')
def update_user(id, name, lastname):
    data = json_manager.read_json('data.json')
    user = next((user for user in data if user['id'] == id), None)
    if user is None:
        click.echo(f'El usuario con id {id} no existe')
        return

    backup_user = user.copy()

    if name:
        user['name'] = name
    if lastname:
        user['lastname'] = lastname

    json_manager.write_json('data.json', data)
    click.echo(f'El usuario con id {id} ha sido actualizado exitosamente')
    click.echo('--------------------------------')
    click.echo('Antes de los cambios:')
    click.echo(f'{backup_user["id"]} - {backup_user["name"]} - {backup_user["lastname"]}')
    click.echo('--------------------------------')
    click.echo('Después de los cambios:')
    click.echo(f'{user["id"]} - {user["name"]} - {user["lastname"]}')

if __name__ == "__main__":
    main()