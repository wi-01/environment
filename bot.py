import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix = '$', intents = intents)

categorías = {
    1 : ["Reducir cantidad de residuos.", "Formas sencillas de disminuir residuos.", "Reducir cantidad de residuos eficientemente.", "1. **Usa botellas y vasos reutilizables**: Lleva contigo una botella de agua reutilizable y un vaso para café. Esto reduce el uso de botellas y vasos desechables. \n2. **Bolsas de compras reutilizables**: Siempre lleva contigo bolsas reutilizables cuando vayas de compras. Esto ayuda a disminuir el uso de bolsas plásticas de un solo uso. \n3. **Compra a granel**: Opta por comprar productos a granel para reducir el uso de empaques innecesarios."],
    2 : ["Opciones de reciclaje.", "Qué cosas reciclar.", "Cosas que se pueden reciclar.", "Puedes reciclar: \n**Papel y Cartón (Contenedor Azul)**: Asegúrate de que estén limpios y secos. No incluyas papel plastificado o sucio. \n**Plástico y Latas (Contenedor Amarillo)**: Limpia los envases antes de reciclar para evitar la contaminación. \n**Vidrio (Contenedor Verde)**: Retira las tapas y enjuaga los envases. No incluyas cristales rotos o espejos. \n**Orgánicos (Contenedor Marrón)**: Usa una compostera si tienes espacio, o deposítalos en el contenedor de orgánicos."],
    3 : ["Recomendaciones.", "Recomendaciones en general.", "Recomendaciones para disminuir residuos y reciclar.", "Compra a granel y evita productos con mucho empaque. \nUsa productos reutilizables como botellas y bolsas. \nPlanifica tus comidas para evitar el desperdicio de alimentos. \nRepara y reutiliza objetos antes de desecharlos. \nDona lo que no uses en lugar de tirarlo. \nSepara tus residuos en papel, plástico, vidrio y orgánicos. \nLimpia los envases antes de reciclarlos. \nComposta tus residuos orgánicos si tienes espacio."],
}

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def cuidar_al_medio_ambiente(ctx, num=None):
    if num is None:
        embed = discord.Embed(title = '¡Formas de cuidar al medio ambiente!', description = '¿Quieres aprender a cuidar el medio ambiente? Ingresa un número para seleccionar una categoría:\n1. Reducir cantidad de residuos\n2. Opciones de reciclaje\n3. Recomendaciones', color=0x32CD32)
        await ctx.send(embed = embed)
    elif num.isdigit() and 1 <= int(num) <= 3:
        num = int(num)
        embed = discord.Embed(title = categorías[num][2], description = categorías[num][3], color = 0x32CD32)
        await ctx.send(embed = embed)
    else:
        embed = discord.Embed(title = '¡Formas de cuidar al medio ambiente!', description = '¿Quieres aprender a cuidar el medio ambiente? Ingresa un número para seleccionar una categoría:\n1. Reducir cantidad de residuos\n2. Opciones de reciclaje\n3. Recomendaciones', color=0x32CD32)
        await ctx.send(embed = embed)
        await ctx.send('Ingrese un número válido (1, 2 o 3)')

bot.run('Token')
