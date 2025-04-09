def analisar_padrao(historico):
    if historico[-5:] == ['🔴'] * 5:
        return '🔵'
    if historico[-5:] == ['🔵'] * 5:
        return '🔴'
    if historico[-4:] == ['🔴', '🔵', '🔴', '🔵']:
        return '🔴'
    if historico[-4:] == ['🔵', '🔴', '🔵', '🔴']:
        return '🔵'
    return None
