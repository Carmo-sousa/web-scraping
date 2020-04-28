TEMPLATE = """
<DOCTYPE html>
<html lang="pt-br">
    <head>
        <title>Lista dos melhores filmes</title>

        <style>
            * {
                font-family: sans-serif;
            }
            h1 {
                font-family: sans-serif;
            }
            table {
                border: 1px solid #333333;
                border-collapse: collapse;
            }
            table thead {
                background: sandybrown;
            }
            td {
                border: 1px solid #333333;
                padding: 5px;
            }
        </style>
    </head>
    <body>
        <h1>Lista com os 20 melhores filmes de todos os tempos!</h1>
        <table>
            <thead>
                <tr>
                    <td>Titulo</td>
                    <td>Lançamento</td>
                    <td>Descricao</td>
                </tr>
            </thead>
            <tbody>
                data_list
            </tbody>
        </table>
    </body>
</html>
"""

URL = "http://www.adorocinema.com/filmes/todos-filmes/notas-espectadores/"
