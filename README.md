Contact Info Manager

This tool is a simple GUI-based application for managing contact information. Users can add new contacts, view existing contacts, and delete contacts from a CSV file. Each contact is stored with a name, phone number, and email address.

Requirements
* Python 3.11.4
* tkinter library (usually included with Python)
* csv library (included with Python)

How to Use the Tool
1. Run the Python script
You can run the script in any Python environment or IDE of your choice (e.g., PyCharm, VS Code, IDLE, etc.).

3. Adding a Contact
* Click the "Add Contact" button.
* Enter the contact's name, phone number, and email address in the respective fields.
* Click the "Add" button to save the contact. A message will confirm that the contact has been added successfully.
3. Viewing Contacts
* Click the "See Contacts" button to open a window displaying all the contacts stored in the contact.csv file.
* Contacts are displayed in a list format, with each contact's name, phone number, and email address.
4. Deleting a Contact
* Click the "Delete Contact" button in the contacts window.
* Enter the name of the contact you wish to delete.
* Click the "Delete" button to remove the contact from the CSV file. A message will confirm whether the contact was found and deleted or not found.

Example Use Case
* Add Contact: You can add a contact named "Tejas Bhardwaj" with a phone number of 1234567890 and email trial@example.com.
* View Contacts: After adding, the contact will appear in the contacts list.
* Delete Contact: If you later wish to delete "Tejas Bhardwaj" from the list, you can do so by entering his name in the deletion prompt.

Notes

The contact data is stored in a CSV file named contact.csv Make sure this file is in the same directory as the script or specify the correct path.
The phone number should be entered as a valid integer, and the script handles basic exceptions to ensure smooth operation.

Enjoy managing your contacts with this simple and intuitive tool!
