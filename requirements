package circleci.test;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

import java.time.Duration;

public class FirstScriptTest {
    public WebDriver driver;

    @Test
    public void eightComponents() {
        driver = new ChromeDriver();

        driver.get("http://localhost");

        String text = driver.findElement(By.id("text")).getText();
        Assertions.assertEquals("", text);
        

        driver.manage().timeouts().implicitlyWait(Duration.ofMillis(500));

        WebElement button = driver.findElement(By.id("button"));
        button.click();
        
        WebElement text2 = driver.findElement(By.id("text"));
        Assertions.assertEquals("Words are CRAAAAZY", text2);

        driver.quit();
    }
}
