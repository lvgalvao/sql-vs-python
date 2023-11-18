import pandas as pd
from pandasql import sqldf

# Função auxiliar para usar pandasql
pysqldf = lambda q: sqldf(q, globals())

# Exemplo de dados
data = {
    "department": ["Sales", "Marketing", "Sales", "HR", "HR", "Marketing"],
    "employee": ["Alice", "Bob", "Eve", "Charlie", "David", "Frank"],
    "salary": [50000, 40000, 55000, 35000, 45000, 38000],
}
df = pd.DataFrame(data)

# Comando SQL
sql_query = """
    SELECT department, AVG(salary) as avg_salary
    FROM df
    WHERE department != 'HR'
    GROUP BY department
    HAVING AVG(salary) < 45000;
"""

# Executando o comando SQL no DataFrame
result = pysqldf(sql_query)
print(result)
