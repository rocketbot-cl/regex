



# Regex
  
Module to work with fixed or complex patterns through Regex  

*Read this in other languages: [English](Manual_regex.md), [Português](Manual_regex.pr.md), [Español](Manual_regex.es.md)*

 ![banner](imgs\Banner_Regex.jpg)

## How to install this module
  
To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The folder name must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, search for the desired module and press install.  


## Description of the commands

### Starts with
  
Detects text strings that begin with a letter or number.
|Parameters|Description|example|
| --- | --- | --- |
|Data|Information to search for words that start with a letter or number|H|
|Text|Text to search for words that start with a letter or number.|Hello world|
|Assign result to variable|Variable that stores the result.|{var}|

### Contains
  
Search for text strings that contain the specified data
|Parameters|Description|example|
| --- | --- | --- |
|Data|Data to search for in the text|Orld|
|Text|Text to search for words that contain the indicated data|Hello World|
|Assign result to variable|Variable that stores the result.|{var}|

### Get dates
  
Gets all dates from the entered text
|Parameters|Description|example|
| --- | --- | --- |
|Text|Text where the date will be obtained|Date: yyyy/mm/dd - dd/mm/yyyy|
|Assign result to variable|Variable where the obtained date is stored|{var}|

### Get phone
  
Get phone numbers from a text
|Parameters|Description|example|
| --- | --- | --- |
|Text|Text where the phone number is obtained|Phone: +18005551212|
|Assign result to variable|Variable where the telephone numbers obtained are stored.|{var}|

### Get email
  
Gets all the emails in a text
|Parameters|Description|example|
| --- | --- | --- |
|Text|Text where the email is obtained|Email: user@example.com|
|Assign result to variable|Variable where the obtained emails are stored|{var}|
