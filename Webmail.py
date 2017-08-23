'''
Created on Jul 20, 2017

@author: Sindura
'''
from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver=webdriver.Firefox()


driver.get("http://demo.automationtesting.in/Register.html")
Sign_in=driver.find_element_by_id("btn2")
Sign_in.click()

'''Full_name=driver.find_element_by_xpath("(//div[@class='col-md-4 col-xs-4 col-sm-4'])[1]")
Full_name.send_keys("Sin")
'''

Full_name=driver.find_element_by_xpath("//input[@placeholder='First Name']")
Full_name.send_keys('Sin')



Last_name=driver.find_element_by_xpath("//input[@placeholder='Last Name']")
Last_name.send_keys("Dura")

Address=driver.find_element_by_xpath("//label[contains(text(),'Address')]/../div[1]")
Address.send_keys('No.14, 8th cross, Hebbal, Bangalore')

Email=driver.find_element_by_xpath("//div[@id='eid'']")
Email.send_keys('abc@abc.com')

Phone=driver.find_element_by_xpath("//form[@id='basicBootstrapForm']/div[4]/div/input")
Phone.send_keys('98765432100')

#//form[@id='basicBootstrapForm']/div[5]/div
list_radio=driver.find_elements_by_xpath("//form[@id='basicBootstrapForm']/div[5]/div/label/input")
for i in list_radio:
    print i.get_attribute('value')
    
list_chk=driver.find_elements_by_xpath("//input[@type='checkbox']")
for i in list_chk:
    print i.get_attribute('value')
    
sel=Select(driver.find_element_by_tag_name("select"))
sel.select_by_index(2)

sel_country=Select(driver.find_element_by_id('countries'))
sel_country.select_by_visible_text('Algeria')

for o in sel_country.options:
        print o.text
'''   
for o in sel_country.options:
    if (sel_country.options[0].text=='Select Country'):
        print o.text
    else: 
        pass
'''
count=sel_country.options
for o in range(1,len(count)):
    print sel_country.options[o].text  
    print count[o].text
    

count1=count
for o in range(1,len(count)):
    #count1[o]=count[o]
    #print count1[o].text
    
#for comparison purpose
    
#count1=count
count.sort()
for o in range(1,len(count1)):
'''if count in count1:
    print "Sucessfull"
else:
    print "Failure"
'''
    if count[o].text==count1[o].text:
        print count[o].text,count1[o].text
else:
    print "-----------"
    
    
'''Slicing [:] creates a duplicate copy rather than referencing the same memory location as lst2=lst1 creates aliases'''
    
    lst1=[4,6,3,7]
    lst2=lst1[:]
    lst1.sort()
    for i in range(len(lst1)):
        if lst1[i]==lst2[i]:
            print lst1[i],lst2[i]
        else:
            print "---------"
        
            
    



print "hello"
    print count[1].text
    '''index out of range: Index Error'''
    #print count[len(count)].text  
    print count[len(count)-1].text '''last element displayed'''
    print count[len(count)-2].text 
    
    
 br1=//input[@id="imagesrc"]    
brow_btn=driver.find_element_by_id("imagesrc")
brow_btn.click()
brow_btn.send_keys("/This PC/Documents/samfile.txt")


'''
wbele=driver.find_element_by_id('basicBootstrapForm')
list=wbele.find_element_by_xpath("//input[@name='radiooptions']")
for i in list:
    print i


list=[]
total=0
for i in driver.find_element_by_xpath("//label[contains(text(),'Gender*')]/../div"):
    list.append(i)
    print list
print 'hi'
'''
'''
for i in driver.find_element_by_xpath("//input[@name='radiooptions']"):
    print i.get_attribute("value")


Gender=driver.find_element_by_xpath("//input[@name='radiooptions'][@value='Male']")
Gender.click()
//form[@id='basicBootstrapForm']/div[2]/div

//form[@id='basicBootstrapForm']/div[4]/div/input

//input[@name='radiooptions'][@value='Male']

//label[contains(text(),'Gender*')]/../div

//div[@id='eid']/input
'''
