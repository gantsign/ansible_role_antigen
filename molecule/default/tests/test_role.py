import pytest


@pytest.mark.parametrize('username', [
    'test_usr1',
    'test_usr2',
])
def test_antigen_install(host, username):
    antigen = host.file('/home/' + username + '/.antigen')
    assert antigen.exists
    assert antigen.is_directory
    assert antigen.user == username
    assert antigen.group in [username, 'users']


@pytest.mark.parametrize('username', [
    'test_usr1',
    'test_usr2',
])
def test_antigen_install_file(host, username):
    antigen = host.file('/home/' + username + '/.antigen/antigen.zsh')
    assert antigen.exists
    assert antigen.is_file
    assert antigen.user == username


@pytest.mark.parametrize('username', [
    'test_usr1',
    'test_usr2',
])
def test_oh_my_zsh_install(host, username):
    antigen = host.file('/home/' + username +
                        '/.antigen/bundles/robbyrussell/oh-my-zsh')
    assert antigen.exists
    assert antigen.is_directory
    assert antigen.user == username
    assert antigen.group in [username, 'users']


@pytest.mark.parametrize('username', [
    'test_usr1',
    'test_usr2',
])
def test_zsh_config(host, username):
    zshrc = host.file('/home/' + username + '/.zshrc')
    assert zshrc.exists
    assert zshrc.is_file
    assert zshrc.user == username
    assert zshrc.group in [username, 'users']
    assert zshrc.contains('source ~/.antigenrc')


@pytest.mark.parametrize('username', [
    'test_usr1',
    'test_usr2',
])
def test_antigen_config(host, username):
    antigenrc = host.file('/home/' + username + '/.antigenrc')
    assert antigenrc.exists
    assert antigenrc.is_file
    assert antigenrc.user == username
    assert antigenrc.group in [username, 'users']
    assert antigenrc.content_string.strip() == r'''
#
# Ansible managed: Do NOT edit this file manually!
#

ZSH_COMPLETIONS_CACHE="$HOME/.antigen/bundles/robbyrussell/oh-my-zsh/cache/completions"
if [[ -d "$ZSH_COMPLETIONS_CACHE" ]]; then
    (( ${fpath[(Ie)"$ZSH_COMPLETIONS_CACHE"]} )) || fpath=("$ZSH_COMPLETIONS_CACHE" $fpath)
fi
unset ZSH_COMPLETIONS_CACHE

source $HOME/.antigen/antigen.zsh

if [[ -d ~/.antigen-etc/use.d ]]; then
    for i in ~/.antigen-etc/use.d/*.zsh; do
        if [ -r $i ]; then
            source $i
        fi
    done
    unset i
fi

if [[ -d ~/.antigen-etc/bundle.d ]]; then
    for i in ~/.antigen-etc/bundle.d/*.zsh; do
        if [ -r $i ]; then
            source $i
        fi
    done
    unset i
fi

[[ -f ~/.antigen-etc/theme.zsh ]] && source ~/.antigen-etc/theme.zsh

antigen apply
'''.strip()  # noqa: E501


def test_simple_theme_config(host):
    theme = host.file('/home/test_usr1/.antigen-etc/theme.zsh')
    assert theme.exists
    assert theme.is_file
    assert theme.user == 'test_usr1'
    assert theme.group in ['test_usr1', 'users']
    assert theme.content_string.strip() == r'''
#
# Ansible managed: Do NOT edit this file manually!
#

antigen theme robbyrussell
'''.strip()


def test_sinple_library_config(host):
    library = host.file('/home/test_usr1/.antigen-etc/use.d/oh-my-zsh.zsh')
    assert library.exists
    assert library.is_file
    assert library.user == 'test_usr1'
    assert library.group in ['test_usr1', 'users']
    assert library.content_string.strip() == r'''
#
# Ansible managed: Do NOT edit this file manually!
#

antigen use oh-my-zsh
'''.strip()


def test_bundle_with_url_config(host):
    bundle = host.file('/home/test_usr1/.antigen-etc/bundle.d/git.zsh')
    assert bundle.exists
    assert bundle.is_file
    assert bundle.user == 'test_usr1'
    assert bundle.group in ['test_usr1', 'users']
    assert bundle.content_string.strip() == r'''
#
# Ansible managed: Do NOT edit this file manually!
#

antigen bundle \
    --url=git
'''.strip()


def test_bundle_with_location_config(host):
    bundle = host.file('/home/test_usr1/.antigen-etc/bundle.d/ant.zsh')
    assert bundle.exists
    assert bundle.is_file
    assert bundle.user == 'test_usr1'
    assert bundle.group in ['test_usr1', 'users']
    assert bundle.content_string.strip() == r'''
#
# Ansible managed: Do NOT edit this file manually!
#

antigen bundle \
    "--url=robbyrussell/oh-my-zsh" \
    --loc=plugins/ant
'''.strip()


def test_theme_with_url_config(host):
    theme = host.file('/home/test_usr2/.antigen-etc/theme.zsh')
    assert theme.exists
    assert theme.is_file
    assert theme.user == 'test_usr2'
    assert theme.group in ['test_usr2', 'users']
    assert theme.content_string.strip() == r'''
#
# Ansible managed: Do NOT edit this file manually!
#

antigen theme https://example.com/testTeme1.git
'''.strip()


def test_advanced_library_config(host):
    library = host.file('/home/test_usr2/.antigen-etc/use.d/prezto.zsh')
    assert library.exists
    assert library.is_file
    assert library.user == 'test_usr2'
    assert library.group in ['test_usr2', 'users']
    assert library.content_string.strip() == r'''
#
# Ansible managed: Do NOT edit this file manually!
#

ENV_TEST1=testValue1

antigen use prezto \
    --verbose
'''.strip()


def test_bundle_with_args_and_env_config(host):
    bundle = host.file('/home/test_usr2/.antigen-etc/bundle.d/mvn.zsh')
    assert bundle.exists
    assert bundle.is_file
    assert bundle.user == 'test_usr2'
    assert bundle.group in ['test_usr2', 'users']
    assert bundle.content_string.strip() == r'''
#
# Ansible managed: Do NOT edit this file manually!
#

ENV_TEST2=testValue2

antigen bundle \
    --url=mvn \
    --no-local-clone
'''.strip()


def test_bundle_with_tag_config(host):
    bundle = host.file('/home/test_usr2/.antigen-etc/bundle.d/gradle.zsh')
    assert bundle.exists
    assert bundle.is_file
    assert bundle.user == 'test_usr2'
    assert bundle.group in ['test_usr2', 'users']
    assert bundle.content_string.strip() == r'''
#
# Ansible managed: Do NOT edit this file manually!
#

ENV_TEST3=testValue3

antigen bundle \
    "--url=https://example.com/gradle.git" \
    --branch=1.0 \
    --no-local-clone
'''.strip()


def test_bundle_with_env_in_value(host):
    bundle = host.file('/home/test_usr2/.antigen-etc/bundle.d/sdkman.zsh')
    assert bundle.exists
    assert bundle.is_file
    assert bundle.user == 'test_usr2'
    assert bundle.group in ['test_usr2', 'users']
    assert bundle.content_string.strip() == r'''
#
# Ansible managed: Do NOT edit this file manually!
#

antigen bundle \
    "--url=$HOME/.sdkman-zsh"
'''.strip()


def test_bundle_url_escaping(host):
    bundle = host.file('/home/test_usr2/.antigen-etc/bundle.d/escape.zsh')
    assert bundle.exists
    assert bundle.is_file
    assert bundle.user == 'test_usr2'
    assert bundle.group in ['test_usr2', 'users']
    assert bundle.content_string.strip() == r'''
#
# Ansible managed: Do NOT edit this file manually!
#

antigen bundle \
    "--url=t\\e\"s\"ti\\ng\`pwd\`test2\$(pwd)"
'''.strip()


def test_console_setup(host):
    # console-setup is Debian family specific
    if host.file('/etc/debian_version').exists:
        setup = host.file('/etc/default/console-setup')
        assert setup.exists
        assert setup.is_file
        assert setup.user == 'root'
        assert setup.group == 'root'
        assert setup.contains('CHARMAP="UTF-8"')
