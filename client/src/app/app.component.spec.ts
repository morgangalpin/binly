/* tslint:disable:no-unused-variable */

import { TestBed, async, getTestBed } from '@angular/core/testing';
import { SocketService } from './shared';
import { AppComponent } from './app.component';
import {} from 'jasmine';

describe('App: Binly', () => {
  let testBed: TestBed;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [
        AppComponent
      ],
      providers: [
        SocketService
      ]
    });
  });

  testBed = getTestBed();

  // it('should create the app', async(() => {
  //   testBed.compileComponents().then(() => {
  //     let fixture = testBed.createComponent(AppComponent);
  //     let app = fixture.debugElement.componentInstance;
  //     expect(app).toBeTruthy();
  //   })
  // }));

  // it(`should have as title 'app works!'`, async(() => {
  //   let fixture = TestBed.createComponent(AppComponent);
  //   let app = fixture.debugElement.componentInstance;
  //   expect(app.title).toEqual('app works!');
  // }));

  // it('should render title in a h1 tag', async(() => {
  //   let fixture = TestBed.createComponent(AppComponent);
  //   fixture.detectChanges();
  //   let compiled = fixture.debugElement.nativeElement;
  //   expect(compiled.querySelector('h1').textContent).toContain('app works!');
  // }));
});
