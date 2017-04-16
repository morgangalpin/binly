/* tslint:disable:no-unused-variable */

import { TestBed, async } from '@angular/core/testing';
import {} from 'jasmine';

import { GpsComponent } from './gps.component';
import { GpsService } from './gps.service';
import { SocketService } from "../shared";

describe('Component: Gps', () => {
  it('should create an instance', () => {
    let component = new GpsComponent(new GpsService(new SocketService()));
    expect(component).toBeTruthy();
  });
});
