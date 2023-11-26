def calculate_p_value(sample, null_hypothesis_mean):
    # Розрахунок середнього значення вибірки
    sample_mean = sum(sample) / len(sample)
    
    # Розрахунок стандартної помилки середнього
    n = len(sample)
    sample_std = (sum([(x - sample_mean) ** 2 for x in sample]) / (n - 1)) ** 0.5 #https://www.uio.no/studier/emner/matnat/math/MAT4010/data/forelesningsnotater/bessel-s-correction---wikipedia.pdf
    standard_error = sample_std / (n ** 0.5)
    
    # Розрахунок t-статистики
    t_statistic = (sample_mean - null_hypothesis_mean) / standard_error
    
    # Розрахунок ступенів свободи
    degrees_of_freedom = n - 1
    
    # Розрахунок p-значення
    from scipy.stats import t #https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.t.html
    p_value = 2 * (1 - t.cdf(abs(t_statistic), degrees_of_freedom))
    
    return p_value

# Приклад використання функції
sample_data = [32, 45, 28, 52, 39, 41, 33, 57, 48, 55]
null_hypothesis_mean = 40
p_value = calculate_p_value(sample_data, null_hypothesis_mean)
print(f'P-значення: {p_value}')
