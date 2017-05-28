/* tslint:disable:no-unused-variable */

import { TestBed, async } from '@angular/core/testing';
import {} from 'jasmine';

import { SteeringComponent } from './steering.component';
import { SteeringService } from './steering.service';
import { SocketService } from "../shared";

describe('Component: Steering', () => {
  it('should create an instance', () => {
    let component = new SteeringComponent(new SteeringService(new SocketService()));
    expect(component).toBeTruthy();
  });
});
