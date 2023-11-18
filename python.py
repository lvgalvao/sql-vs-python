import pandas as pd

# Exemplo de dados
data = {
    "department": ["Sales", "Marketing", "Sales", "HR", "HR", "Marketing"],
    "employee": ["Alice", "Bob", "Eve", "Charlie", "David", "Frank"],
    "salary": [50000, 40000, 55000, 35000, 45000, 38000],
}


# Funções correspondentes às cláusulas SQL
def select(df, columns):
    return print(df[columns])


def where(df, condition):
    return df.query(condition)


def group_by(df, columns):
    return df.groupby(columns)


def avg(grouped_df):
    # Calcula a média apenas das colunas numéricas e reseta o índice
    return grouped_df.mean(numeric_only=True).reset_index()


# Aplicando as operaçõ                                                                          `es
FROM = pd.DataFrame(data)
WHERE_DF = where(FROM, "department != 'HR'")
GROUP_BY_DF = group_by(WHERE_DF, "department")
AVG_DF = avg(GROUP_BY_DF)
HAVING_CONDITION = AVG_DF[AVG_DF["salary"] < 45000]
SELECT = select(HAVING_CONDITION, ["department", "salary"])
