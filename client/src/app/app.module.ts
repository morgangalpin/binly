import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';
import { MaterialModule } from '@angular/material';

import { AppComponent } from './app.component';

// Shared module
import { SharedModule } from "./shared/shared.module";

import { ArmModule } from './arm/arm.module';
import { ServoModule } from './servo/servo.module';
import { CameraModule } from './camera/camera.module';
import { GpsModule } from './gps/gps.module';
import { SteeringModule } from './steering/steering.module';
import { ThrottleModule } from './throttle/throttle.module';

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpModule,
    MaterialModule,

    SharedModule,

    // Custom Modules
    ArmModule,
    ServoModule,
    CameraModule,
    GpsModule,
    SteeringModule,
    ThrottleModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
