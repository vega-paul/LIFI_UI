import { test as base, chromium, type BrowserContext } from "@playwright/test";
const { setExpectInstance } = require("@synthetixio/synpress/commands/playwright");
const { resetState } = require("@synthetixio/synpress/commands/synpress");

export const test = base.extend<{
    context: BrowserContext;
}>({
    context: async ({ }, use) => {
        // required for synpress as it shares same expect instance as playwright
        await setExpectInstance(expect);

        // use existing metamask extension
        const metamaskPath = "./extensions/metamask";

        // prepare browser args
        const browserArgs = [
            `--disable-extensions-except=${metamaskPath}`,
            `--load-extension=${metamaskPath}`,
            "--remote-debugging-port=9222",
        ];

        if (process.env.CI) {
            browserArgs.push("--disable-gpu");
        }

        if (process.env.HEADLESS_MODE) {
            browserArgs.push("--headless=new");
        }

        // launch browser
        const context = await chromium.launchPersistentContext("", {
            headless: false,
            args: browserArgs,
        });

        // wait for metamask
        const pages = context.pages();
        if (pages.length > 0 && pages[0]) {
            await pages[0].waitForTimeout(3000);
        }

        // Skip MetaMask setup for now - just verify browser works
        console.log('Skipping MetaMask wallet initialization for basic infrastructure test');

        await use(context);

        await context.close();

        await resetState();
    },
});

export const expect = test.expect;