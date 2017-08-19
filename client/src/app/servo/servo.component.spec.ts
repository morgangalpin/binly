/* tslint:disable:no-unused-variable */

import { TestBed, async } from '@angular/core/testing';
import {} from 'jasmine';

import { ServoComponent } from './servo.component';
import { ServoFormatterSet } from './ServoFormatterSet';
import { SocketService, SimpleSocketService } from "../shared";

describe('Component: Servo', () => {
  it('should create an instance', () => {
    let component = new ServoComponent('test', 0, 10, 1, new SocketService(), new ServoFormatterSet());
    expect(component).toBeTruthy();
  });
});
