# pyvirtualdisplay-bug

Trying to reproduce/isolate the issue causing Ubuntu 22.04 LTS tests action
to crash on [this workflow](https://github.com/Becheler/quetzal-CRUMBS/blob/main/.github/workflows/unit_tests.yml). I suspect interactions between Pyvirtualdisplay, pytest and mayavi to be the main cause.

See [this issue](https://stackoverflow.com/questions/72874772/pytest-core-dump-on-unbutu-22-04-lts?noredirect=1#comment128730685_72874772) on stackoverflow.

Branches description:

- `main`: the bug as initially found on my own repo.
- `fix`: a bug-free branch that uses only 2 dependencies in the `requirements.txt` (but I need more deps in real life)
- `break_again`: a branch that reproduces the bug after restoringg and cleaning the `requirements.txt` a little bit.
- `cutting_deps`: a branch were I tried to add one dep at a time until it breaks again: pyqt5==5.15.7 breaks the working behavior of mayavi==4.7.4 + 
PyVirtualDisplay==3.0

