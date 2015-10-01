from distutils.core import setup
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'mundipaggOnePython'))

setup(
    name='mundipagg_one_python',
    version='1.0.0',
    package_dir={'mundipaggOnePython': 'mundipaggOnePython', 'data_contracts': 'mundipaggOnePython/data_contracts', 'enum_types': 'mundipaggOnePython/enum_types', 'resource_clients': 'mundipaggOnePython/resource_clients', 'transaction_report_file': 'mundipaggOnePython/transaction_report_file'},
    packages=['mundipaggOnePython', 'data_contracts', 'enum_types', 'resource_clients', 'transaction_report_file'],
    url='https://github.com/mundipagg/mundipagg-one-python',
    license='Apache',
    author='Newton Rocha',
    author_email='nrocha@mundipagg.com',
    description='Sdk for integration with mundipagg payment api',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Gateway Integration :: SDK',

        'License ::  Apache 2 License',

        'Programming Language :: Python :: 2.7'
    ],
    install_requires=['requests>=2.0.0', 'enum34>=1.0.0', 'xmltodict>=0.9.2'],
    keywords=['mundipagg', 'rest', 'sdk', 'payments']
)
