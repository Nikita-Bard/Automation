from lesson_7.calculator.pages.Calcmainpage import CalcMain


def test_calculator(chrome_browser):
    calcmain = CalcMain(chrome_browser)
    calcmain.insert_time()
    calcmain.clicking_buttons()
    assert '15' in calcmain.wait_button_gettext()
