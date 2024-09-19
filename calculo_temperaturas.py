def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el monto del descuento dado un monto total y un porcentaje de descuento.

    :param monto_total: El monto total de la compra.
    :param porcentaje_descuento: El porcentaje de descuento (por defecto es 10%).
    :return: El monto del descuento calculado.
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento


def main():
    # Primer ejemplo de uso
    monto1 = 100.0
    descuento1 = calcular_descuento(monto1)
    monto_final1 = monto1 - descuento1
    print(f'Monto total: {monto1}, Descuento: {descuento1}, Monto final: {monto_final1}')

    # Segundo ejemplo de uso
    monto2 = 200.0
    porcentaje2 = 15
    descuento2 = calcular_descuento(monto2, porcentaje2)
    monto_final2 = monto2 - descuento2
    print(f'Monto total: {monto2}, Descuento: {descuento2}, Monto final: {monto_final2}')


if __name__ == "__main__":
    main()
