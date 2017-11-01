import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MatCardModule } from '@angular/material';

import { CameraComponent } from './camera.component';
import { CameraService } from './camera.service';

@NgModule({
  imports: [
    CommonModule,
    MatCardModule
  ],
  declarations: [CameraComponent],
  providers: [
    CameraService
  ],
  exports: [CameraComponent]
})
export class CameraModule { }
