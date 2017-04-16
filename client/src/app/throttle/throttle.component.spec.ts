/* tslint:disable:no-unused-variable */

import { TestBed, async } from '@angular/core/testing';
import {} from 'jasmine';

import { ThrottleComponent } from './throttle.component';
import { ThrottleService } from './throttle.service';
import { SocketService } from "../shared";

describe('Component: Throttle', () => {
  it('should create an instance', () => {
    let component = new ThrottleComponent(new ThrottleService(new SocketService()));
    expect(component).toBeTruthy();
  });
});
