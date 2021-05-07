from decorators import make_html


def test_make_html():
    @make_html('p')
    @make_html('span')
    @make_html('strong')
    def get_text(text='I code with PyBites'):
        """Returns the text"""
        return text

    assert get_text() == '<p><span><strong>I code with PyBites</strong></span></p>'
    assert get_text.__doc__ == 'Returns the text'


def test_make_html_with_params():
    @make_html('p')
    @make_html('span')
    @make_html('strong')
    def get_text(text='I code with PyBites'):
        return text

    assert get_text('some content') == '<p><span><strong>some content</strong></span></p>'
