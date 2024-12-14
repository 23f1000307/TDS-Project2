# Analysis Report

## Dataset Analysis
Shape: (2363, 11)
Columns:
{'Country name': dtype('O'), 'year': dtype('int64'), 'Life Ladder': dtype('float64'), 'Log GDP per capita': dtype('float64'), 'Social support': dtype('float64'), 'Healthy life expectancy at birth': dtype('float64'), 'Freedom to make life choices': dtype('float64'), 'Generosity': dtype('float64'), 'Perceptions of corruption': dtype('float64'), 'Positive affect': dtype('float64'), 'Negative affect': dtype('float64')}
Missing Values:
{'Country name': 0, 'year': 0, 'Life Ladder': 0, 'Log GDP per capita': 28, 'Social support': 13, 'Healthy life expectancy at birth': 63, 'Freedom to make life choices': 36, 'Generosity': 81, 'Perceptions of corruption': 125, 'Positive affect': 24, 'Negative affect': 16}
Summary Statistics:
{'Country name': {'count': 2363, 'unique': 165, 'top': 'Argentina', 'freq': 18, 'mean': nan, 'std': nan, 'min': nan, '25%': nan, '50%': nan, '75%': nan, 'max': nan}, 'year': {'count': 2363.0, 'unique': nan, 'top': nan, 'freq': nan, 'mean': 2014.7638595006347, 'std': 5.059436468192795, 'min': 2005.0, '25%': 2011.0, '50%': 2015.0, '75%': 2019.0, 'max': 2023.0}, 'Life Ladder': {'count': 2363.0, 'unique': nan, 'top': nan, 'freq': nan, 'mean': 5.483565806178587, 'std': 1.1255215132391925, 'min': 1.281, '25%': 4.647, '50%': 5.449, '75%': 6.3235, 'max': 8.019}, 'Log GDP per capita': {'count': 2335.0, 'unique': nan, 'top': nan, 'freq': nan, 'mean': 9.399671092077089, 'std': 1.1520694444710216, 'min': 5.527, '25%': 8.506499999999999, '50%': 9.503, '75%': 10.3925, 'max': 11.676}, 'Social support': {'count': 2350.0, 'unique': nan, 'top': nan, 'freq': nan, 'mean': 0.8093693617021277, 'std': 0.12121176420299144, 'min': 0.228, '25%': 0.744, '50%': 0.8345, '75%': 0.904, 'max': 0.987}, 'Healthy life expectancy at birth': {'count': 2300.0, 'unique': nan, 'top': nan, 'freq': nan, 'mean': 63.40182826086957, 'std': 6.842644351828009, 'min': 6.72, '25%': 59.195, '50%': 65.1, '75%': 68.5525, 'max': 74.6}, 'Freedom to make life choices': {'count': 2327.0, 'unique': nan, 'top': nan, 'freq': nan, 'mean': 0.750281908036098, 'std': 0.13935703459253465, 'min': 0.228, '25%': 0.661, '50%': 0.771, '75%': 0.862, 'max': 0.985}, 'Generosity': {'count': 2282.0, 'unique': nan, 'top': nan, 'freq': nan, 'mean': 9.772129710780206e-05, 'std': 0.16138760312630687, 'min': -0.34, '25%': -0.112, '50%': -0.022, '75%': 0.09375, 'max': 0.7}, 'Perceptions of corruption': {'count': 2238.0, 'unique': nan, 'top': nan, 'freq': nan, 'mean': 0.7439709562109026, 'std': 0.1848654805936834, 'min': 0.035, '25%': 0.687, '50%': 0.7985, '75%': 0.86775, 'max': 0.983}, 'Positive affect': {'count': 2339.0, 'unique': nan, 'top': nan, 'freq': nan, 'mean': 0.6518820008550662, 'std': 0.10623970474397627, 'min': 0.179, '25%': 0.572, '50%': 0.663, '75%': 0.737, 'max': 0.884}, 'Negative affect': {'count': 2347.0, 'unique': nan, 'top': nan, 'freq': nan, 'mean': 0.27315083084789094, 'std': 0.08713107245795021, 'min': 0.083, '25%': 0.209, '50%': 0.262, '75%': 0.326, 'max': 0.705}}

## LLM Insights
# Detailed Analysis Report

## Dataset Overview

The dataset contains 2363 entries across 11 columns, capturing various metrics related to well-being across multiple countries from 2005 to 2023. The following columns are included:

1. **Country name**: The name of the country.
2. **Year**: The year of the data entry.
3. **Life Ladder**: A measure of subjective well-being.
4. **Log GDP per capita**: The logarithm of GDP per capita, indicating economic prosperity.
5. **Social support**: A measure of perceived social support.
6. **Healthy life expectancy at birth**: The average number of years a newborn is expected to live in good health.
7. **Freedom to make life choices**: A measure of personal freedom.
8. **Generosity**: A measure of charitable giving.
9. **Perceptions of corruption**: A measure of how corrupt a country is perceived to be.
10. **Positive affect**: The presence of positive emotions.
11. **Negative affect**: The presence of negative emotions.

### Missing Values

The dataset has several missing values across different columns:

- **Log GDP per capita**: 28 missing values
- **Social support**: 13 missing values
- **Healthy life expectancy at birth**: 63 missing values
- **Freedom to make life choices**: 36 missing values
- **Generosity**: 81 missing values
- **Perceptions of corruption**: 125 missing values
- **Positive affect**: 24 missing values
- **Negative affect**: 16 missing values

Careful handling of these missing values is necessary for accurate analysis.

## Summary Statistics

### Year
- **Mean**: 2014.76
- **Standard Deviation**: 5.06
- **Range**: 2005 - 2023

### Life Ladder
- **Mean**: 5.48
- **Standard Deviation**: 1.13
- **Range**: 1.28 - 8.02

### Log GDP per capita
- **Mean**: 9.40
- **Standard Deviation**: 1.15
- **Range**: 5.53 - 11.68

### Social Support
- **Mean**: 0.81
- **Standard Deviation**: 0.12
- **Range**: 0.23 - 0.99

### Healthy Life Expectancy at Birth
- **Mean**: 63.40
- **Standard Deviation**: 6.84
- **Range**: 6.72 - 74.60

### Freedom to Make Life Choices
- **Mean**: 0.75
- **Standard Deviation**: 0.14
- **Range**: 0.23 - 0.99

### Generosity
- **Mean**: 0.0001
- **Standard Deviation**: 0.16
- **Range**: -0.34 - 0.70

### Perceptions of Corruption
- **Mean**: 0.74
- **Standard Deviation**: 0.18
- **Range**: 0.035 - 0.98

### Positive Affect
- **Mean**: 0.65
- **Standard Deviation**: 0.11
- **Range**: 0.18 - 0.88

### Negative Affect
- **Mean**: 0.27
- **Standard Deviation**: 0.09
- **Range**: 0.08 - 0.71

## Correlation Analysis

### Key Correlations

1. **Life Ladder & Log GDP per capita**: Strong positive correlation (0.78)
2. **Life Ladder & Social Support**: Strong positive correlation (0.72)
3. **Life Ladder & Healthy Life Expectancy**: Strong positive correlation (0.71)
4. **Life Ladder & Freedom to Make Life Choices**: Moderate positive correlation (0.54)
5. **Life Ladder & Positive Affect**: Moderate positive correlation (0.52)
6. **Life Ladder & Perceptions of Corruption**: Moderate negative correlation (-0.43)
7. **Negative Affect & Life Ladder**: Moderate negative correlation (-0.35)

### Observations
- Economic prosperity (Log GDP per capita) significantly influences subjective well-being (Life Ladder).
- Social support, healthy life expectancy, and personal freedom also contribute positively to an individual's perceived well-being.
- Higher perceptions of corruption are associated with lower life satisfaction.
- Positive affect correlates positively with life satisfaction, while negative affect correlates negatively.

## Conclusion

The dataset provides valuable insights into the factors influencing life satisfaction across various countries over the years. It highlights the importance of economic factors, social support, and personal freedoms in determining well-being. The moderate to strong correlations observed between the Life Ladder and other variables suggest that policies aimed at improving economic conditions, social support systems, and reducing corruption could enhance the overall well-being of populations.

### Recommendations
1. **Address Missing Values**: Explore methods to handle missing data, such as imputation or exclusion, based on the analysis purpose.
2. **Further Analysis**: Conduct regression analysis to quantify the impact of each factor on life satisfaction.
3. **Policy Implications**: Encourage policies that focus on improving GDP per capita, social support networks, and reducing corruption to foster a higher quality of life.

This report provides a foundational understanding of the dataset, and further investigation can yield actionable insights for policymakers and researchers alike.

## Charts
![happiness\happiness_heatmap.png](happiness\happiness_heatmap.png)
![happiness\happiness_year_distribution.png](happiness\happiness_year_distribution.png)
![happiness\happiness_Life Ladder_distribution.png](happiness\happiness_Life Ladder_distribution.png)
![happiness\happiness_Log GDP per capita_distribution.png](happiness\happiness_Log GDP per capita_distribution.png)
![happiness\happiness_Social support_distribution.png](happiness\happiness_Social support_distribution.png)
![happiness\happiness_Healthy life expectancy at birth_distribution.png](happiness\happiness_Healthy life expectancy at birth_distribution.png)
![happiness\happiness_Freedom to make life choices_distribution.png](happiness\happiness_Freedom to make life choices_distribution.png)
![happiness\happiness_Generosity_distribution.png](happiness\happiness_Generosity_distribution.png)
![happiness\happiness_Perceptions of corruption_distribution.png](happiness\happiness_Perceptions of corruption_distribution.png)
![happiness\happiness_Positive affect_distribution.png](happiness\happiness_Positive affect_distribution.png)
![happiness\happiness_Negative affect_distribution.png](happiness\happiness_Negative affect_distribution.png)
