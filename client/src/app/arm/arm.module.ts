import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { MatCardModule } from '@angular/material';

import { ArmComponent } from './arm.component';

import { ServoModule } from '../servo/servo.module';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    MatCardModule,

    // Custom modules.
    ServoModule
  ],
  declarations: [ArmComponent],
  exports: [ArmComponent],
  providers: []
})
export class ArmModule { }
