import pandas as pd

# Exemplo de dados
data = {
    "department": ["Sales", "Marketing", "Sales", "HR", "HR", "Marketing"],
    "employee": ["Alice", "Bob", "Eve", "Charlie", "David", "Frank"],
    "salary": [50000, 40000, 55000, 35000, 45000, 38000],
}
FROM = pd.DataFrame(data)

# Assegurando que a coluna 'salary' é numérica
FROM["salary"] = pd.to_numeric(FROM["salary"], errors="coerce")


# Funções correspondentes às cláusulas SQL
def select(df, columns):
    return df[columns]


def where(df, condition):
    return df.query(condition)


def group_by(df, columns):
    return df.groupby(columns)


def avg(grouped_df):
    # Calcula a média apenas das colunas numéricas e reseta o índice
    return grouped_df.mean(numeric_only=True).reset_index()


# Aplicando as operações
WHERE_DF = where(FROM, "department != 'HR'")
GROUP_BY_DF = group_by(WHERE_DF, "department")
AVG_DF = avg(GROUP_BY_DF)

# Aplicando a condição equivalente à cláusula HAVING
HAVING_CONDITION = AVG_DF["salary"] < 45000
AVG_HAVING_CONDITION_DF = AVG_DF[HAVING_CONDITION]

# Selecionando as colunas finais para exibir
RESULTADO = select(AVG_HAVING_CONDITION_DF, ["department", "salary"])
print(RESULTADO)
