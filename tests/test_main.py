import main


def test_main_prints_prediction(capsys):
    main.main()

    captured = capsys.readouterr()

    assert captured.out.strip() == "1"
