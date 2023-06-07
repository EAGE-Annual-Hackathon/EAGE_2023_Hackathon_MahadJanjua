import sketch
import pandas as pd

def test_sketch():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    result = df.sketch.ask("what are the values of column A", call_display=False)
    print(result)
    """with open("data.html", "w") as file:
        file.write(result)"""
#test_sketch()
