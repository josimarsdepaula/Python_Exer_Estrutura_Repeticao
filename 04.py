populacao_a = 80000
populacao_b = 200000
taxa_anual_cresc_a = 0.03
taxa_anual_cresc_b = 0.015

anos = 0
while populacao_a <= populacao_b:
    populacao_a = populacao_a * (1 + taxa_anual_cresc_a)
    populacao_b = populacao_b * (1 + taxa_anual_cresc_b)
    anos += 1
print(f"Serão necessários {anos} anos")