def assert_equal_csv(csv1, csv2):
    assert len(csv1) == len(csv2), "CSVs have different number of rows"
    for row1, row2 in zip(csv1, csv2):
        assert len(row1) == len(row2), "Rows have different number of columns"
        for cell1, cell2 in zip(row1, row2):
            assert cell1 == cell2, f"Cells are not equal: {cell1} != {cell2}"

def assert_equal_json(json1, json2):
    assert json1 == json2, f"JSONs are not equal: {json1} != {json2}"