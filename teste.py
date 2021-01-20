from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time;
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install());
driver.implicitly_wait(40);
driver.get("http://localhost:333");

time.sleep(2);

driver.find_element_by_xpath("//*[text()='Cadastrar']").click();

element = driver.find_element_by_xpath("//input[@placeholder='Marca...']").send_keys('Teste');
element = driver.find_element_by_xpath("//input[@placeholder='Modelo...']").send_keys('Teste ');
element = driver.find_element_by_xpath("//input[@placeholder='Placa-mãe...']").send_keys('Teste');
element = driver.find_element_by_xpath("//input[@placeholder='Memória RAM...']").send_keys('2');
element = driver.find_element_by_xpath("//input[@placeholder='Capacidade HD...']").send_keys('2');
element = driver.find_element_by_xpath("//input[@placeholder='Marca HD...']").send_keys('teste');
element = driver.find_element_by_xpath("//input[@placeholder='Processador...']").send_keys('Asus');
element = driver.find_element_by_xpath("//input[@placeholder='Velocidade Processador...']").send_keys('2');
element = driver.find_element_by_xpath("//input[@placeholder='URL da Imagem']").send_keys('path//teste');

time.sleep(2);

driver.find_element_by_xpath("//*[text()='Cadastrar']").click();

time.sleep(2);

driver.find_element_by_xpath("//*[text()='Teste']").click();
time.sleep(2);

driver.find_element_by_xpath("//*[text()=' Editar']").click();
time.sleep(2);
element = driver.find_element_by_xpath("//input[@placeholder='Marca...']").clear();
time.sleep(2);
element = driver.find_element_by_xpath("//input[@placeholder='Marca...']").send_keys('Teste edicao');
time.sleep(2);
driver.find_element_by_xpath("//*[text()='Alterar']").click();
time.sleep(2);
driver.find_element_by_xpath("//*[text()='Teste edicao']").click();
time.sleep(2);
driver.find_element_by_xpath("//*[text()=' Deletar']").click();

