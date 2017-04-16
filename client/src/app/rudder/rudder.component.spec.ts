/* tslint:disable:no-unused-variable */

import { TestBed, async } from '@angular/core/testing';
import {} from 'jasmine';

import { RudderComponent } from './rudder.component';
import { RudderService } from './rudder.service';
import { SocketService } from "../shared";

describe('Component: Rudder', () => {
  it('should create an instance', () => {
    let component = new RudderComponent(new RudderService(new SocketService()));
    expect(component).toBeTruthy();
  });
});
