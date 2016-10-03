import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MaterialModule } from '@angular/material';

import { CameraComponent } from './camera.component';

@NgModule({
  imports: [
    CommonModule,
    MaterialModule
  ],
  declarations: [CameraComponent],
  exports: [CameraComponent]
})
export class CameraModule { }
