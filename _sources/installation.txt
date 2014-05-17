
Installation
=============================

install using pip:

``pip install git+ssh://git@github.com/ajmirsky/ansible-role-manager.git``

or if you're interested in contributing, install the source:

``pip install -e git+ssh://git@github.com/ajmirsky/ansible-role-manager.git#egg=ansible-role-manager``

.. WARNING::

    For those on MacOSX running Xcode5.1, there is a breaking change which turns a previous warning when compiling `pycrypto` 
    into an error. To use the legacy behavior, set the environment variable::

    >> export ARCHFLAGS='-Wno-error=unused-command-line-argument-hard-error-in-future'

    Excerpt from XCode Release Notes::

        Apple LLVM compiler in Xcode 5.1 treats unrecognized command-line options as errors. This issue has been
        seen when building both Python native extensions and Ruby Gems, where some invalid compiler options are
        currently specified. Projects using invalid compiler options will need to be changed to remove those
        options. To help ease that transition, the compiler will temporarily accept an option to downgrade
        the error to a warning:
    
        -Wno-error=unused-command-line-argument-hard-error-in-future

    For more information, see the `XCode 5.1 Release Notes`_


..  _XCode 5.1 Release Notes: https://developer.apple.com/library/mac/releasenotes/DeveloperTools/RN-Xcode/xc5_release_notes/xc5_release_notes.html    






