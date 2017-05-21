import { BinlyPage } from './app.po';

describe('binly App', function() {
  let page: BinlyPage;

  beforeEach(() => {
    page = new BinlyPage();
  });

  it('should display message saying app works', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('app works!');
  });
});
