import { DuckomaticPage } from './app.po';

describe('duckomatic App', function() {
  let page: DuckomaticPage;

  beforeEach(() => {
    page = new DuckomaticPage();
  });

  it('should display message saying app works', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('app works!');
  });
});
