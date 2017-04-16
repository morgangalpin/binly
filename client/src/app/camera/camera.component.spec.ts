/* tslint:disable:no-unused-variable */

import { TestBed, async } from '@angular/core/testing';
import {} from 'jasmine';

import { CameraComponent } from './camera.component';
import { CameraService } from './camera.service';
import { SocketService } from "../shared";

describe('Component: Camera', () => {
  it('should create an instance', () => {
    let component = new CameraComponent(new CameraService(new SocketService()));
    expect(component).toBeTruthy();
  });
});
