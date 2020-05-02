def __getattr__(name):
    import poetry.masonry.api

    if name in ("build_wheel", "build_sdist"):
        # Do something before building
        pass

    return getattr(poetry.masonry.api, name)
