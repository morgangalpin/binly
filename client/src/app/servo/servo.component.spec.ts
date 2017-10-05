/* tslint:disable:no-unused-variable */

import { TestBed, async } from '@angular/core/testing';
import {} from 'jasmine';

import { ServoComponent } from './servo.component';
import { LeftRightFormatterSet } from '../formatter';
import { SocketService, SimpleSocketService } from "../shared";

describe('Component: Servo', () => {
  it('should create an instance', () => {
    let component = new ServoComponent(new SocketService(), new LeftRightFormatterSet());
    expect(component).toBeTruthy();
  });
});
