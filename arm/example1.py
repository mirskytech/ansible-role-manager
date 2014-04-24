
from git import Repo


def main():

    
    _url, _path = 'git@git.mirsky.net:ansible-playbooks/haproxy.git','.cache/haproxy'
    #repo = Repo.clone_from(_url, _path)
    #repo.git.checkout('tags/real')

    pip_path = 'git://git.myproject.org/MyProject.git@abcdee'
    
    import re
    fqdn = '((?:[a-z][a-z\\.\\d\\-]+)\\.(?:[a-z][a-z\\-]+))(?![\\w\\.])'
    repo = '((?:[a-z][a-z0-9_]+))'
    gitre = re.compile(r'git\:\/\/' + fqdn +'\/' + repo + '\.git' + '@?' + repo+'?', re.IGNORECASE)
    
    print gitre.search(pip_path).groups()
    
    repo = Repo(_path)
    repo.git.checkout('bafd95f5054eceba952f555600313bc1a2d72e70')
    


main()