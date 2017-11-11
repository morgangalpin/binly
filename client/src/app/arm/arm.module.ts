import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { MatCardModule } from '@angular/material';
import { FlexLayoutModule } from '@angular/flex-layout';

import { ArmComponent } from './arm.component';

import { MacrosModule } from './macros/macros.module';
import { ServoModule } from '../servo/servo.module';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    MatCardModule,
    FlexLayoutModule,

    // Custom modules.
    MacrosModule,
    ServoModule
  ],
  declarations: [ArmComponent],
  exports: [ArmComponent],
  providers: []
})
export class ArmModule { }
