import subprocess


def convert_ui_to_py(directory: str, input_ui: str, output_py: str):
    subprocess.run(
        ["python", "-m", "PyQt5.uic.pyuic", "-x", "-o", output_py, input_ui],
        cwd=directory,
        check=True
    )


convert_ui_to_py(
    directory="C:\\Users\\user\\PycharmProjects\\Calculate\\ui\\Designe\\",
    input_ui="LrfDesigner.ui",
    output_py="Lrf.py"
)
print('success')