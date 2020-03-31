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
  download_url = 'https://github.com/saudzi/quadratic-equation-saudzi/archive/0.1.tar.gz',   
  keywords = ['quadratic''quadeq''equation'],  
  install_requires=[            
          'cmath',
          
      ],
  classifiers=[
    'Development Status :: 4 - Beta',        
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',     
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)