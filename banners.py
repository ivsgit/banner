def banner_text(text: str = " ", screen_width: int = 80) -> None:  # adding DEFAULT values for the parameters!

    """
    Takes in two arguments, one str type and one int type; if the arguments satisfy the function, displays text
    arguments centred according to the integer argument, which will be used as the width. Raises an error if the
    integer is greater than the text length
    :param text: any character, including a white space.
    :param screen_width: an integer that will serve as a reference for the banner's width.
    :raises ValueError: raises an error if the integer value is lesser than the text size.
    """

    if len(text) > screen_width - 4:
        raise ValueError(f"String '{text}' is larger than specified width: {screen_width}")
    if text == "*":
        print("*" * screen_width)

    else:
        output_string = f"**{text.center(screen_width - 4)}**"
        print(output_string)


banner_text("*", 60)
banner_text("Oh it's a jolly 'oliday with Mary", 60)
banner_text("Mary makes your 'eart so light!", 60)
banner_text("When the day is gray and ordianry,", 60)
banner_text("Mary makes the sun shine bright!", 60)
banner_text("Oh, 'appiness is bloomin' all around 'er,", 60)
banner_text()  # using default argument, or:
banner_text(screen_width=60)
banner_text("The daffodils are smilin' at the dove,", 60)
banner_text("When Mary 'olds your 'and,", 60)
banner_text("You feel so grand!", 60)
banner_text("Your 'eart starts beatin' like", 60)
banner_text("A big brass band!", 60)
banner_text("It's a jolly 'oliday with Mary...", 60)
banner_text("No wonder that it's Mary that we love!", 60)
banner_text("*", 60)


