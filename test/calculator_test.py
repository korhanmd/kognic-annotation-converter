from annotation_converter.calculator import calculate_coordinates

def test_case_1():
    test_data = [[
                  324.02301025390625,
                  594.9812622070312
                ], [
                  253.24899291992188,
                  628.365234375
                ], [
                  171.12440490722656,
                  605.6641235351562
                ], [
                  253.9166717529297,
                  549.5790405273438
                ]]
    assert calculate_coordinates(test_data) == [247.5737075805664,
                                                588.9721374511719,
                                                152.8986053466797,
                                                78.78619384765625]

def test_case_2():
    test_data = [[
                  645.1768798828125,
                  671.0967407226562
                ], [
                  467.5741271972656,
                  764.5718994140625
                ], [
                  334.0382080078125,
                  658.4108276367188
                ], [
                  496.2843322753906,
                  566.938720703125
                ]]
    assert calculate_coordinates(test_data) == [489.6075439453125,
                                                665.7553100585938,
                                                311.138671875,
                                                197.6331787109375]

def test_case_3():
    test_data = [[
                  754.6763305664062,
                  546.9083251953125
                ], [
                  721.2923583984375,
                  572.9478759765625
                ], [
                  691.9144287109375,
                  548.2437133789062
                ], [
                  721.2923583984375,
                  516.195068359375
                ]]
    assert calculate_coordinates(test_data) == [723.2953796386719,
                                                544.5714721679688,
                                                62.76190185546875,
                                                56.7528076171875]

def test_case_4():
    test_data = [[
                  724.3621826171875,
                  554.1156616210938
                ], [
                  718.6283569335938,
                  557.4492797851562
                ], [
                  713.8279418945312,
                  553.7156372070312
                ], [
                  718.2283325195312,
                  551.0487670898438
                ]]
    assert calculate_coordinates(test_data) == [719.0950622558594,
                                                554.2490234375,
                                                10.53424072265625,
                                                6.4005126953125]

def test_case_5():
    test_data = [[
                  1002.4415283203125,
                  533.6742553710938
                ], [
                  958.6953735351562,
                  556.4222412109375
                ], [
                  926.3232421875,
                  536.2990112304688
                ], [
                  954.3207397460938,
                  507.4265441894531
                ]]
    assert calculate_coordinates(test_data) == [964.3823852539062,
                                                531.9243927001953,
                                                76.1182861328125,
                                                48.995697021484375]
    