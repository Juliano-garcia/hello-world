from IPython.display import HTML
import random
def get_answer(eid):

    with open("load/answers/{}.html".format(eid), 'r') as f:
        data = f.read()

    js_f_name = 'code_toggle_{}'.format(str(random.randint(1,2**64)))
    html = """
    <div id="{div}" style="display: none;">{answer}</div>
    <script>
        function {f_name}() {{
            var x = document.getElementById("{div}");
            if (x.style.display === "none") {{
                x.style.display = "block";
            }} else {{
                x.style.display = "none";
            }}
        }}
    </script>
    <button onclick="javascript:{f_name}()">Show / Hide Answer</button>
    """\
        .format(answer=data, div='div_'+eid, f_name=js_f_name)

    return HTML(html)