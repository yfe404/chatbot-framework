from setuptools import setup, find_packages

setup(
    name='chatbot_framework',
    packages=find_packages(exclude=["tests", "tools"]),
    version=0.1
)

print("\nWelcome to Chatbot Framework!")
