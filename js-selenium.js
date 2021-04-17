// npm install selenium-webdriver
// npm install chromedriver

// to run this script, type: node js-selenium.js

const { Builder, By, Key, until } = require("selenium-webdriver");
const chrome = require("selenium-webdriver/chrome");
const chromedriver = require("chromedriver");

chrome.setDefaultService(new chrome.ServiceBuilder(chromedriver.path).build());

(async function example() {
  let driver = await new Builder().forBrowser("chrome").build();
  try {
    await driver.get("https://www.github.com/fahmiauliarahman");
    // this one will wait until the title is same as you type in the params.
    // await driver.wait(until.titleIs("fahmiauliarahman (Fahmi Aulia Rahman) · GitHub"), 1000);

    // use one of these selector..
    // this code is used to get the element by name attribute on html
    // await driver
    //   .findElement(By.name("q"))
    //   .sendKeys(
    //     "anything, or you can use keyboard button like this ->",
    //     Key.RETURN
    //   );
    // this one is used to get the element by id
    // await driver.findElement(By.id("find-by-id")).sendKeys("anything");
    // this one is used to get the element by xpath (recommended)
    // await driver.findElement(By.xpath("find-by-xpath")).sendKeys("anything");
  } finally {
    // quit from browser:
    // await driver.quit();
  }
})();
