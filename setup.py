from distutils.core import setup
setup(
  name = 'quadratic-equation-saudzi',         
  packages = ['quadratic-equation-saudzi'],   
  version = '0.1',      
  license='MIT',       
  description = 'just a simple tool to solve quadratic equations',  
  author = 'saba udzilauri',                  
  author_email = 'sabaxbox1@gmail.com',     
  url = 'https://github.com/saudzi',  
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['quadratic''quadeq''equation'],  
  install_requires=[            # I get to this in a second
          'validators',
          'beautifulsoup4',
      ],
  classifiers=[
    'Development Status :: 4 - Beta',     
    'Intended Audience :: begginer developers',     
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',     
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)