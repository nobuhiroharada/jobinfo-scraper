import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

KEY = os.environ['ENV_KEY']

total_projects = ['total_projects']

target_programs_frameworks = [
                                'php', 'laravel', 'cakephp', 'wordpress',
                                'ruby', 'rails',
                                'python', 'django', 'flask',
                                'java', 'spring', 'struts', 'kotlin',
                                'javascript', 'react', 'vue', 'jquery',
                                'swift', 'objective-c',
                                'go',
                                'gcp', 'aws', 'azure',
                                'linux',
                                'git', 'svn',
                                'jenkins', 'circle',
                                'mysql', 'postgresql', 'oracle', 'sql server', 
                                'sql', 
                                
                            ]

url_levtech = 'https://freelance.levtech.jp/project/search/'
url_crowdtech = 'https://crowdtech.jp/job_offers'