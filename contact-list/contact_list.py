import re
import json
import sys

class Contact:
    def __init__(self, name, phone_number, email_address):
        self.name = name
        self.phone_number = phone_number
        self.email_address = email_address

    def update_contacts_option(self, field):
        user_option = input(f'Enter new {field} (Press Enter to skip): ')
        return user_option if user_option else None

    def delete_contact_option(self):
        return input('Confirm contact deletion (Y/N): ').lower() == 'y'

class ContactList:
    def __init__(self):
        self.contacts = []

    def add_contact(self):
        name = input('Enter your full name: ').capitalize()
        phone_number = input('Enter your phone number: ')
        email_address = input('Enter your email address: ')

        contact = Contact(name, phone_number, email_address)
        self.contacts.append(contact)
        self.save_contacts()

    def search_contact(self):
        name = input('Enter the contact to search: ').capitalize()
        found_contacts = [contact for contact in self.contacts if contact.name == name]

        if found_contacts:
            for contact in found_contacts:
                print(f'Name: {contact.name}, Phone: {contact.phone_number}, Email: {contact.email_address}')
        else:
            print('Contact not found.')

    def view_contacts(self):
        for contact in self.contacts:
            print(f'Name: {contact.name}, Phone: {contact.phone_number}, Email: {contact.email_address}')

    def update_contacts(self):
        name = input('Enter the contact name to update: ').capitalize()
        found_contact = next((contact for contact in self.contacts if contact.name == name), None)

        if found_contact:
            phone_number = found_contact.update_contacts_option('phone number')
            email_address = found_contact.update_contacts_option('email address')

            if phone_number:
                found_contact.phone_number = phone_number
            if email_address:
                found_contact.email_address = email_address

            self.save_contacts()
            print('Contact updated successfully.')
        else:
            print('Contact not found.')

    def delete_contact(self):
        name = input('Enter the contact to delete: ').capitalize()
        found_contact = next((contact for contact in self.contacts if contact.name == name), None)

        if found_contact:
            if found_contact.delete_contact_option():
                self.contacts.remove(found_contact)
                self.save_contacts()
                print('Contact deleted')
            else:
                print('Contact deletion cancelled.')
        else:
            print('Contact not found.')

    def save_contacts(self):
        with open('store_contacts.json', 'w') as json_file:
            json.dump([{'Name': contact.name, 'Phone Number': contact.phone_number, 'Email Address': contact.email_address}
                       for contact in self.contacts], json_file)

    def main_menu(self):
        while True:
            print('\n********** Welcome to Contacts **********')
            print('_________________________________________')
            print('A. Add contact\nV. View list of Contacts\nS. Search for Contacts\n'
                  'U. Update Contacts\nD. Delete Contacts\nQ. Quit')
            print('_________________________________________')      
            
            menu_option = input('Select an option: ').lower()

            if menu_option == 'a':
                self.add_contact()
            elif menu_option == 'v':
                self.view_contacts()
            elif menu_option == 's':
                self.search_contact()
            elif menu_option == 'u':
                self.update_contacts()
            elif menu_option == 'd':
                self.delete_contact()
            elif menu_option == 'q':
                print('Exiting. Thank you!')
                sys.exit(0)
            else:
                print('Invalid option. Please try again.')

if __name__ == "__main__":
    contact_list = ContactList()
    contact_list.main_menu()
